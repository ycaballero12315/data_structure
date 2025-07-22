class LoggerMixin:
    def log(self, msg):
        return f'[LOG] {msg}'
    
class DataBase:
    def conn(self):
        return 'Conectando...'
    
class App(DataBase, LoggerMixin):
    def eject(self):
        return(
            self.log('Init DataBase...'),
            self.conn(),
            self.log('End connection DataBase...'))
        
app = App()

print(app.eject())
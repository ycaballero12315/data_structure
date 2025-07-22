class Translator:
    def __init__(self):
        self.store_translator = {}
    
    def add_translator(self,es_string, en_string):
        self.store_translator[es_string] = en_string

    def search_translator(self,es_string):
        return self.store_translator.get(es_string,"No se a encontrado la traduccion")
    
    def show_dictionary(self):
        for es_string, en_string in self.store_translator.items():
            print(f"{es_string}: {en_string}")

def main():
    trans = Translator()
    trans.add_translator("hola", "hello")
    trans.add_translator("te veo mannana", "I see you tomorrow")
    trans.add_translator("adios", "Goobye")
    
    print("Traducir:")
    frase = input("Frase que va a traducir: ")
    print(f"La traduccion de: {frase}: {trans.search_translator(frase)}")

    print("Palabras traducidas: ")
    trans.show_dictionary()

if __name__ == "__main__":
    main()


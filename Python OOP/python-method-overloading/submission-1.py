class TextProcessor:
    # Implement method overloading for format_text method
    # def format_text(self, text1: str, text2: str = None) -> str:
    #     if(text2 == None):
    #         return text1.upper()
    #     else :
    #         return text1+text2 

    def format_text(self, *arg) -> str:
        if (len(arg) == 2):
            return arg[0] + arg[1]
        else:
            return arg[0].upper()

# Don't modify the code below
processor = TextProcessor()
print(processor.format_text("hello"))
print(processor.format_text("hello", "world"))

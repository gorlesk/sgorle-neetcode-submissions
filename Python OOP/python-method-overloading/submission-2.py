class TextProcessor:
    # Implement method overloading for format_text method
    # def format_text(self, text1: str, text2: str = None) -> str:
    #     if(text2 == None):
    #         return text1.upper()
    #     else :
    #         return text1+text2 

    def format_text(self, *argmts) -> str:
        if (len(argmts) == 2):
            return argmts[0] + argmts[1]
        else:
            return argmts[0].upper()

# Don't modify the code below
processor = TextProcessor()
print(processor.format_text("hello"))
print(processor.format_text("hello", "world"))

def validate_steam_ascii(ascii_art):
    # Boşluklar ve satır atlamalar dahil ham karakter sayısını hesaplar
    char_count = len(ascii_art)
    
    print("-" * 30)
    print(f"Veri Hacmi: {char_count} Karakter")
    
    if char_count < 1000:
        print("Durum: ONAYLANDI (Steam limitleri içerisinde)")
    else:
        print(f"Durum: REDDEDİLDİ (Sınır {char_count - 1000} karakter aşıldı)")
    print("-" * 30)

# Test edilecek ASCII sanatını üçlü tırnak arasına yapıştırın
test_verisi = r"""
       _                        
       \ ` * - .                    
         )     _ ` - .                 
       .      :   ` .   .                
       :   _        '    \               
       ;   * ` _ .       ` * - . _          
       ` -.- '                         `-.       
         ;                 `               `.     
         : .                 .               \    
         .   \      .       :      . - '      .   
         '     ` + . ;     ;     '            :   
         :     '      |         ;              ; - . 
         ;    '       :   : ` - :         _ .` *  ;
   . * '   /    . * '   ;   . * ` - +'   ` * ' 
   ` * - *     ` * - *    ` * - * '⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""

validate_steam_ascii(test_verisi)
floppy_disk_size = 1.44
books_pages = 100
lines_pages = 50
symbol_lines = 25
simvol_na_stanitzah = lines_pages * symbol_lines
knigi_c_sranitzami = simvol_na_stanitzah * books_pages
Obhom_knigi_bait = knigi_c_sranitzami * 4
Obhom_knigi_Kbait = Obhom_knigi_bait / 1024
Obhom_knigi_Mbait = Obhom_knigi_Kbait / 1024
Kolichestvo_knig = floppy_disk_size / Obhom_knigi_Mbait
# TODO Найдите количество книг, которое можно разместить на дискете

print("Количество книг, помещающихся на дискету:", round(Kolichestvo_knig))

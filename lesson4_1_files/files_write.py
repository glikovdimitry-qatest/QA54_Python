with open("test.txt","w", encoding="utf-8") as file:
    file.write("Hello")
    file.write("Alex")

# file = open("test.txt","w",encoding="utf-8")
# file.write("Hello Kris")
# file.close()

#"r" - read (В существующий файл)
#"w" - write (Создаёт и перезаписывает)
#"a" - append (Добавляет в конец не стирая содержимое файла)
#"rb", "wd" pdf, screenshot
def log_res(test_name,status):
    with open("test_1.txt","a",encoding="utf-8") as file:
        file.write(f"{test_name}: {status}\n")
log_res("test_register","PASSED")
log_res("test_login","FAILED")
log_res("test_logout","PASSED")


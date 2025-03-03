try :
    with open('file.txt' , 'r') as f:
        data = f.read()
        print(data)
except Exception as e :
    print(f"There is a error , {e}")
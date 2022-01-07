from tkinter import *

# 내용 삭제
def delete() :
    global items
    selection = listbox.curselection() # 리스트 박스 내에서 마우스 커서가 선택한 것
    if (len(selection) == 0) : # 선택 안 하면
        return # 돌아가기
    
    value = listbox.get(selection[0]) # value = 커서가 선택한 것
    ind = items.index(value) # items 리스트 내의 value 값 위치
    del items[ind] # times 리스트에서 [ind] 위치에 있는 값 삭제
    listbox.delete(selection[0]) # 리스트 박스에서 삭제하기

# 내용 생성
def add(event) :
    global items
    items.append(entry.get()) # 엔트리 입력창에서 얻은 값 itmes 리스트 끝에 추가
    listbox.insert(END, entry.get()) # 마지막으로 들어간 문장 밑에 추가
    entry.delete(0, 'end') # 엔트리 창 지우기

window = Tk() # 윈도우 생성
window.title("2022_Seoul_Hardware_Hackathon") # 윈도우 타이틀 설정
window.geometry("500x300") # 윈도우 크기 설정

items = [] # 리스트 박스 내의 내용이 들어 갈 공백 리스트 생성

# 리스트 박스 생성
listbox = Listbox(window, height = 0, selectmode = "extended") # Listbox 생성, selectmode에 대한 설명은 밑에 참고
# 리스트 박스에 데이터 추가
for i in range(len(items)): # 아이템 자료 개수만큼 반복하는데
    listbox.insert(END, itmes[i]) # 리스트 박스 끝에 자료 추가
listbox.pack() # 리스트 박스 보이기

buttonDel = Button(window, width = 10, text = "Delete", overrelief = "solid", command = delete)
# 삭제 버튼 생성, overrelief는 마우스 커서를 위에 올렸을 때의 반응, solid는 검은 테두리 씌우기, 버튼 누르면 delete 함수 실행
buttonDel.pack() # 삭제 버튼 보이기

# Entry 생성
entry = Entry(window, width = 30)
entry.bind("<Return>", add) # enter 키가 입력되었을 때 add 함수 실행
entry.pack() # entry 창 보이기

window.mainloop() # 윈도우 창 보이기
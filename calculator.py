import flet as ft

def main(page: ft.Page):
    page.title = "เครื่องคิดเลข"
    page.window_width = 300
    page.window_height = 400
    page.window_resizable = False

    # กล่องแสดงผลลัพธ์
    result = ft.TextField(value="", text_align="right", width=280, read_only=True)

    # ฟังก์ชันเมื่อกดปุ่ม
    def button_clicked(e):
        if e.control.text == "=":
            try:
                result.value = str(eval(result.value))
            except:
                result.value = "Error"
        elif e.control.text == "C":
            result.value = ""
        else:
            result.value += e.control.text
        page.update()

    # ปุ่มตัวเลขและเครื่องหมาย
    buttons = [
        ["7", "8", "9", "/"],
        ["4", "5", "6", "*"],
        ["1", "2", "3", "-"],
        ["C", "0", "=", "+"],
    ]

    # สร้าง layout ปุ่ม
    rows = []
    for row in buttons:
        rows.append(
            ft.Row(
                controls=[
                    ft.ElevatedButton(text=btn, width=60, height=60, on_click=button_clicked)
                    for btn in row
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            )
        )

    # เพิ่ม widget ลงหน้า
    page.add(
        ft.Column(
            controls=[result] + rows,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

# รันแอป
ft.app(target=main)

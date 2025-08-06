import flet as ft
import csv
import os

CSV_FILE = "register.csv"

def main(page: ft.Page):
    page.title = "ฟอร์มการรับสมัคร"
    page.window_width = 400
    page.window_height = 400

    # สร้าง input fields
    name_input = ft.TextField(label="ชื่อ-สกุล", width=300)
    phone_input = ft.TextField(label="เบอร์โทรศัพท์", width=300, keyboard_type=ft.KeyboardType.PHONE)
    team_input = ft.TextField(label="ชื่อทีม", width=300)

    status_text = ft.Text(color="green")

    def submit_form(e):
        name = name_input.value.strip()
        phone = phone_input.value.strip()
        team = team_input.value.strip()

        if not name or not phone or not team:
            status_text.value = "❌ กรุณากรอกข้อมูลให้ครบ"
            status_text.color = "red"
        else:
            file_exists = os.path.isfile(CSV_FILE)
            with open(CSV_FILE, mode="a", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                # เขียนหัวตารางถ้าไฟล์ยังไม่มี
                if not file_exists:
                    writer.writerow(["ชื่อ-สกุล", "เบอร์โทรศัพท์", "ชื่อทีม"])
                writer.writerow([name, phone, team])

            # ล้างค่า input fields และแจ้งสถานะบันทึกสำเร็จ
            name_input.value = ""
            phone_input.value = ""
            team_input.value = ""
            status_text.value = "✅ บันทึกข้อมูลเรียบร้อย"
            status_text.color = "green"

        page.update()

    submit_button = ft.ElevatedButton(text="ส่งข้อมูล", on_click=submit_form)

    page.add(
        ft.Column(
            controls=[
                name_input,
                phone_input,
                team_input,
                submit_button,
                status_text,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

ft.app(target=main)

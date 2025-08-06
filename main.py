import flet as ft
import csv
def main(page: ft.Page):
    page.title ="FORM"
    page.window.width = 350
    page.window.height = 500
    page.padding = 20
    page.bgcolor="#9f3636"
    
    name = ft.TextField(label="Full Name")
    phone = ft.TextField(label="Phone")
    team = ft.TextField(label="Team Name")
    result = ft.Text()

    def save_data(e):
        with open("register.cvs", "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            # writer.writerow([""])
            list = f"Name[ {name.value} ], Phone[ {phone.value} ], Team[ {team.value} ]"
            writer.writerow([list])

        result.value = "save successfully!!!!!!!!!!!"
        name.value = ""
        phone.value =""
        team.value =""
        page.update()

    button = ft.ElevatedButton("Save", on_click=save_data)

    page.add(
        ft.Text("Register", size=30, weight="bold"),
        name,
        phone,
        team,
        button,
        result
        )
ft.app(target=main)

from helpers import clean_screen
from json import load
from PIL import Image, ImageTk
from canvas import frame,root
from tkinter import Button
from json import dump


def display_products():
    clean_screen()
    display_stock()


def display_stock():  # admin database admin panel

    with open("db/products.json", "r") as stock:
        info = load(stock)

    x, y = 150, 50

    for item_name, item_info in info.items():
        item_img = ImageTk.PhotoImage(Image.open(item_info["image"]))
        images.append(item_img)

        frame.create_text(x, y, text=item_name, font=("Comic Sans MS", 15))
        frame.create_image(x, y + 100, image=item_img)

        if item_info["quantity"] >0:
            color = "green"
            text = f"In stock: {item_info['quantity']}"

            item_button = Button(
                root,
                text="Buy",
                bg="green",
                fg="white",
                font=("Comic Sans Ms",12),
                width=5,
                command=lambda x=item_name,y=info:buy_produuct(x,y)
            )

            frame.create_window(x,y+230,window=item_button)
        else:
            color = "red"
            text= "Out of stock"
        frame.create_text(x,y+180,text=text,fill=color,font=("Comic Sans Ms",12))

        x += 200

        if x > 550:
            y += 230
            x = 150
def buy_produuct(product_name,info):
    info[product_name]["quantity"] -= 1

    with open("db/products.json","w") as stock:
        dump(info,stock)

    display_products()


images= []
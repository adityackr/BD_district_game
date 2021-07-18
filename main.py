import turtle, pandas

screen = turtle.Screen()
screen.setup(width=507, height=720)
screen.title("Bangladesh District Game")
image = "Bangladesh_subdistricts.gif"
screen.addshape(image)
turtle.shape(image)

# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)

# turtle.mainloop()


data = pandas.read_csv("bd_districts.csv")
districts = data.district.to_list()
guessed_district = []

while len(guessed_district) < 64:
  input_district = screen.textinput(title=f"{len(guessed_district)}/64 Correct Districts", prompt="What's another district's name?").title()

  if input_district == "Exit":
    missing_district = []
    for district in districts:
      if district not in guessed_district:
        missing_district.append(district)
    new_data = pandas.DataFrame(missing_district)
    new_data.to_csv("districts_to_learn.csv")
    break
  elif input_district in districts:
    guessed_district.append(input_district)
    t= turtle.Turtle()
    t.hideturtle()
    t.penup()
    district_data = data[data.district == input_district]
    t.goto(int(district_data.x), int(district_data.y))
    t.write(input_district)

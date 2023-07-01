import flet as ft
from flet import TextField, Text, Column, border, Row,ResponsiveRow,CrossAxisAlignment,Image, colors, Page, AppBar,colors,Container,FLET_APP,alignment,ElevatedButton,padding



def main(page: Page):
    page.bgcolor='BLACK'
    page.padding=20
    page.appbar = AppBar(title=Text("I-CODERS"),center_title=True,bgcolor='ORANGE')
    page.horizontal_alignment = 'center'

    lit = ft.ResponsiveRow([
    ft.Container
    (
        content = Text(value = " Free Programming Courses ",
        size= 20,
        color='BLACK',
        
        ),
       bgcolor='WHITE',
       height=35,
       border_radius = 6 ,
       alignment = alignment.center_left,
       
    ),
      ],
    )
   
    row = Row (
        [
        ft.Container
    (
        content= Image(
        src="https://logowik.com/content/uploads/images/911_c_logo.jpg",
        width=210,
        height=160,col={"md": 4}),

       bgcolor='WHITE', 
       width = 1200,
       padding = 2,
       expand = 1,
       height = 130,
       border_radius = 10,
       alignment = alignment.center,
    ), 
    ft.Container
    (
        content= Image(
        src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRJZtOrjhh0SWX0v1Ulsi-H8wcmIYJjfiUsmPgKjxUF8lRdptGQK4JNpGu1fBh8UkW41Hw&usqp=CAU",
       width=210,
       height=130,col={"md": 4}),
       bgcolor='WHITE', 
       width = 1200, 
       padding = 2,
       expand = 1,
       height = 130,
       border_radius = 10,
       alignment = alignment.center,
    ), 
    
    
        ],
        width=1200,
    )
    
    row1 = Row (
        [
        ft.Container
    (
        content= Image(
        src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/61/HTML5_logo_and_wordmark.svg/2048px-HTML5_logo_and_wordmark.svg.png",
        width=210,
        height=110,col={"md": 4}),

       bgcolor='WHITE', 
       width = 1200,
       padding = 2,
       expand = 1,
       height = 130,
       border_radius = 10,
       alignment = alignment.center,
    ), 
    ft.Container
    (
        content= Image(
        src="https://cdn.freebiesupply.com/logos/large/2x/css3-logo-png-transparent.png",
       width=210,
       height=130,col={"md": 4}),
       bgcolor='WHITE', 
       width = 1200, 
       padding = 2,
       expand = 1,
       height = 130,
       border_radius = 10,
       alignment = alignment.center,
    ), 
    
    
        ],
        width=1200,
    )
    row2 = Row (
        [
        ft.Container
    (
         ft.OutlinedButton(text="Load More",width=300,height=45),
       bgcolor='TRANSPARENT', 
       width = 1200, 
       padding = 2,
       expand = 1,
       height = 80,
       border_radius = 10,         
       alignment = alignment.center,
    ), 
        ],
        width=1200,
    )
    row3 = Row (
        [
            
        ft.Container
    (
       TextField (label="Enter Email",border_color='WHITE',),
       bgcolor='TRANSPARENT', 
       width = 1200, 
       padding = 2,
       expand = 1,
       height = 80,
       border_radius = 10,         
       alignment = alignment.center,
    ), 
        ],
        width=1200,
    )
   
    row4 = Row (
        [
        ft.Container
    (
       TextField (label="Your Feedback",border_color='WHITE',),
       bgcolor='TRANSPARENT', 
       width = 1200, 
       padding = 2,
       expand = 1,
       height = 80,
       border_radius = 10,         
       alignment = alignment.center,
    ), 
        ],
        width=1200,
    )
    
    row5 = Row (
        [
        ft.Container
    (
         ft.OutlinedButton(text="Submit Now",width=160,height=45,),
       bgcolor='TRANSPARENT', 
       width = 1200, 
       padding = 2,
       expand = 1,
       height = 80,
       border_radius = 10,         
       alignment = alignment.center,
    ), 
        ],
        width=1200,
    )

    page.add(lit,row,row1,row2,row3,row4,row5)
ft.app(target=main)

from typing import Sized
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.recycleview import RecycleView

from kivy.properties import ObjectProperty,ListProperty
import sqlite3


class MyGridLayout(Widget):
    
    first_name = ObjectProperty(None)
    last_name = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def submit(self):
        # get text from input
        firstname = self.first_name.text
        lastname = self.last_name.text
        email = self.email.text
        password = self.password.text

        conn = sqlite3.connect('student.db')
        with conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO Student VALUES(?, ?, ?, ?)', (firstname, lastname, email, password))
            conn.commit()

        print(f'First Name: {firstname}')
        print(f'Last Name: {lastname}')
        print(f'email: {email}')
        self.ids.firstname.text = ''
        self.ids.lastname.text = ''
        self.ids.email.text = ''
        self.ids.password.text = ''


    def fetch_all(self):
        conn = sqlite3.connect('student.db')
        with conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM Student')
            all_rows = cursor.fetchall()
            res=''
           
            for row in all_rows:
                res+='{'
                for name,col in zip(['first-name','last-name','email'],row[:-1]):
                    res+=f'{name}:{col},  '
                res+='}\n'
            self.ids.output_label.text = res
            self.ids.output_label.size = self.width,len(all_rows)*50
    def clear(self):
        self.ids.output_label.text = ''
        self.ids.output_label.size = self.width,0
class MyApp(App):
    def build(self):
        self.title='Student Registration By 18BCE191'
        
        # create connection
        conn = sqlite3.connect('student.db')
        
        # obtain cursor
        cursor = c = conn.cursor()

        c.execute("""CREATE TABLE if not exists Student(
            email text primary key, first_name text, last_name text,password text)
		 """)
        
        # commit
        conn.commit()

		# Close our connection
        conn.close()
        return MyGridLayout()


if __name__ == '__main__':
    MyApp().run()


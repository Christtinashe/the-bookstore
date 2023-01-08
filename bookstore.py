 # Importing our library
import sqlite3   

#function to enter book
def enter_book():
    title = input('Please Enter the Book Title: ')
    author = input('Please Enter the Author Name: ')
    qty = input('Please Enter the quantity of {} available: '.format(title))
    #inserting the values
    cur.execute('INSERT INTO books(title, author, qty) values (?, ?, ?)', (title, author, qty))
    #saving the changes  
    db.commit()   

#a function to update a book 
def update_book():
    id = input('Please Enter the id of book that you want to update: ')
    title = input('Please Enter the new title: ')
    author = input('Please Enter the updated author name: ')
    qty = input('Please Enter the new quantity: ')
    # setting the new values
    cur.execute('UPDATE books SET title=?, author=?, qty=? WHERE id=?', (title, author, qty, id))    
    #saving the changes
    db.commit()

# a function to delete a book 
def delete_book():
    id = input('Please Enter the book id to delete: ')
    cur.execute('SELECT title from books WHERE id=?', (id,))
    #fetching one entry fom the above executed statement
    results = cur.fetchone()    
    print(results)
    if results:
        choice = input('please confirm you want to delete the book with id {}(1/0): '.format(results[0]))
    else:
        print('No book with the requested id was found')
        return
    if choice == '1':
        cur.execute('DELETE FROM books WHERE id=?', (id,))
    db.commit()

#a function to search for a book
def search_book():
    author = input('Input the author name to search book for: ')

    cur.execute('SELECT * FROM books where author like ?', (author,))
    #fexhing results from the above staement
    results = cur.fetchall()    
    if results:
        for row in results:
            print(str(row[0]) + ' | ' + row[1] + ' | ' + row[2] + ' | ' + str(row[3]))
    else:
        print('No books found')


if __name__ == '__main__':
    db = sqlite3.connect('bookstore.db')
    cur = db.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS books('
               'id integer primary key AUTOINCREMENT,'
                'Title varchar(255),'
               'Author varchar(30),'
               'Qty integer)')
    #while statement with bookstore menu option to choose from
    while True:
        choice = input('1. Enter Book\n'
                       '2. Update Book\n'
                       '3. Delete Book\n'
                       '4. Search Book\n'
                       '0. Exit: ')
        if choice == '1':
            enter_book()
        elif choice == '2':
            update_book()
        elif choice == '3':
            delete_book()
        elif choice == '4':
            search_book()
        elif choice == '0':
            break
        else:
            print('Wrong Choice,please Try again...')

    print('Thank you for visiting our BookStore until next time!!')
    db.close()
// Importing modules
import React, { useState, useEffect } from "react";
import "./App.css";
  
function App() {

    const [bookList, setBooklist] = useState([]);
    // usestate for setting a javascript
    // object for storing and using data
    const [data, setdata] = useState({
        name: "",
        publish_year: 0,
        key: "",
        isbn: "",
    });

    const bookListStuff = fetch("/book").then((res) =>
        res.json().then((data) => {
            // console.log("data is  ", data.data)
            setBooklist(data.data)

            // console.log("printing stuff ", bookList)
            // data.data.map(book => {
            //     console.log(book.title)
            //     return (
            //         <li>
            //             {book.title}
            //         </li>
            //     )
            // })
        }
        ));

  
    return (
        <div className="App">
            <header> 
                <h1>Automated Textbook Download</h1>
            </header>
                <div>
                    {bookList.map((book) => (
                        <>
                        <p key={book.title}>{book.title}</p>
                        <p key={book.publish_year}>{book.publish_year}</p>
                        <p key={book.key}>{book.key}</p>
                        <p key={book.isbn}>{book.isbn}</p>
                        <br></br>
                        </>
                    ))}
                </div>
        </div>
    );
}
  
export default App;
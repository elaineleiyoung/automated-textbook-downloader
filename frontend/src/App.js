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
        author: "",
        isbn: "",
        img: ""
    });

    fetch("/book").then((res) =>
        res.json().then((data) => {
            // console.log("data is  ", data.data)
            setBooklist(data.data)
        }
        ));

    // fetch("https://covers.openlibrary.org/b/isbn/0486600904.jpg").then((res) =>
    //     res.json().then((data) => {
    //         // console.log("data is  ", data.data)
    //         setBooklist(data.data)
    // }
    // ));

  
    return (
        <div className="App">
            <header> 
                <h1>Automated Textbook Download</h1>
            </header>
                <div>
                    {bookList.map((book) => (
                        <>
                        <h2 key={book.title}>{book.title}</h2>
                        <p key={book.publish_year}>Publication Year: {book.publish_year}</p>
                        <p key={book.author}>Author: {book.author_name.join(", ")}</p>
                        <p key={book.isbn[0]}>ISBN: {book.isbn[0]}</p>
                        <img src={`https://covers.openlibrary.org/b/id/${book.cover_i}-M.jpg`} />
                        <br></br>
                        </>
                    ))}
                </div>
        </div>
    );
}
  
export default App;
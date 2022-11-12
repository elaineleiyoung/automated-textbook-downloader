import React from 'react'

export default function SearchTextbooks(placeholder, data) {
  return (
    <div className='search'>
        <div className='searchInputs'>
            <input type='text' placeholder={placeholder}/>
            <div className='searchIcon'></div>
        </div>


        <div className='dataResults'></div>
    </div>
  )
}

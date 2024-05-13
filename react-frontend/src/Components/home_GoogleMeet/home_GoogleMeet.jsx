import React from 'react';
import './home_GoogleMeet.css'; // Import CSS file
import { Link } from 'react-router-dom';

function HomeGoogleMeet() {
  return (
    <div>
      <header>
        <button className="home-title"><a href="/">
          <h2>Google Suite Manager Tool</h2></a></button>
        <Link to='/sign_in'>
          <button className="sign-in-button">
            <p>Sign In</p></button></Link>
      </header>

      <section2>
      <Link to='/home_GoogleMeet'>
        <button className="meeting-button">
            <h1 className="meeting-title"> Google Meet </h1>
          </button></Link>
      <Link to='/home_GoogleCalendar'>
        <button className="calendar-button">
            <h1 className="calendar-title"> Google Calendar </h1>
        </button></Link>
      </section2>

      <section>
        <nav>
          <h1 className="to-do-list-title"> To Do List: </h1>
          <ul>
            <li><a href="#">London</a></li>
            <li><a href="#">Meeting w/ Prof</a></li>
            <li><a href="#">Coding HTML</a></li>
            <li><a href="#">Open Source HW#4</a></li>
            <li><a href="#">Team Meeting</a></li>
            <li><a href="#">Complete Forms</a></li>
            <li><a href="#">Leadership Assignment</a></li>
          </ul>
        </nav>

        <article>
          <label htmlFor="eventname">Meeting Title: </label>
          <input type="text" id="eventname" name="eventname" /><br /><br />
          <label htmlFor="date">Meeting Date: </label>
          <input type="text" id="date" name="date" /><br /><br />
          <label htmlFor="info">Description: </label>
          <input type="text" id="info" name="info" /><br /><br />

          <a href="/"><input type="submit" value="Submit" /></a>
          <a href="/"><input type="submit" value="Cancel" /></a>
        </article>
      </section>

      <footer>
        <p>Footer</p>
      </footer>
    </div>
  );
}

export default HomeGoogleMeet;

import React from 'react';
import './home_GoogleCalendar.css'; // Import CSS file
import { Link } from 'react-router-dom';

function HomeGoogleCalendar() {
  return (
    <div>
      <header>
        <button className="home-title"><a href="/">
          <h2>Google Suite Manager Tool</h2></a></button>
          <Link to='/sign_in'>
            <button className="sign-in-button">
            <p>Sign In</p></button></Link>
      </header>

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
          <label htmlFor="eventname">Task: </label>
          <input type="text" id="eventname" name="eventname" />
          <label htmlFor="date">Due Date: </label>
          <input type="text" id="date" name="date" /><br /><br />
          <label htmlFor="info">Description: </label>
          <input type="text" id="info" name="info" /><br /><br />

          <input type="radio" id="Appointment" name="fav_language" value="Appointment" />
          <label htmlFor="Appointment">Appointment</label>
          <input type="radio" id="Focus" name="fav_language" value="Focus" />
          <label htmlFor="Focus">Focus Time</label>
          <input type="radio" id="Task" name="fav_language" value="Task" />
          <label htmlFor="Task">Task</label>
          <input type="radio" id="Event" name="fav_language" value="Event" />
          <label htmlFor="Event">Event</label>

          <br /><br />

          <a href="/"><input type="submit" value="Submit" /></a>
          <a href="/"><input type="submit" value="Cancel" /></a>
        </article>
      </section>

      <div className="calendar-container">
        <h2>Google Calendar</h2>
        <div className="calendar">
          <iframe src="https://calendar.google.com/calendar/embed?height=600&wkst=1&ctz=America%2FNew_York&bgcolor=%23ffffff&src=czExMjE2MjEwNTJAZ21haWwuY29t&src=Njg3OGJmODc3YjE4OGFiNGE5MzcxNDI5NDhmYjg5ZmZhYjE4ODMyMzU0MzY5ZmE4ZjcxNGZkOGY0YzdjMTVmNEBncm91cC5jYWxlbmRhci5nb29nbGUuY29t&src=YWRkcmVzc2Jvb2sjY29udGFjdHNAZ3JvdXAudi5jYWxlbmRhci5nb29nbGUuY29t&src=ZmFtaWx5MDcwMzQ1NTk1NzU3MTUwMjk1MzhAZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ&src=ZW4udXNhI2hvbGlkYXlAZ3JvdXAudi5jYWxlbmRhci5nb29nbGUuY29t&color=%23cc003c&color=%237986CB&color=%2333B679&color=%23F09300&color=%230B8043" style={{ border: 'solid 1px #777' }} width="800" height="600" frameBorder="0" scrolling="no"></iframe>
        </div>
      </div>

      <footer>
        <p>Footer</p>
      </footer>
    </div>
  );
}

export default HomeGoogleCalendar;

import React from 'react';
import { Link } from 'react-router-dom';

function Home() {
  return (
    <div>
      <header>
        <h2>Google Suite Manager Tool</h2>
        <button className="sign-in-button">
          <Link to="/sign_in">
            <p>Sign In</p>
          </Link>
        </button>
      </header>

      <section2>
        <button className="meeting-button">
          <Link to="/home_GoogleMeet">
            <h1 className="meeting-title"> Google Meet </h1>
          </Link>
        </button>
        <button className="calendar-button">
          <Link to="/home_GoogleCalendar">
            <h1 className="calendar-title"> Google Calendar </h1>
          </Link>
        </button>
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
      </section>

      <footer>
        <p>Footer</p>
      </footer>
    </div>
  );
}

export default Home;

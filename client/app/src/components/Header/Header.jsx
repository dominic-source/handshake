import "./Header.css";
import { NavLink } from "react-router-dom";

function LandNav() {
  return (
    <nav>
      <header className="header">
        <div className="container">
          <NavLink to="/" className="logo">
            HANDSHAKE
          </NavLink>

          <input className="menu-btn" type="checkbox" id="menu-btn" />
          <label className="menu-icon" htmlFor="menu-btn">
            <span className="navicon"></span>
          </label>
          <ul className="menu">
            <li>
              <NavLink to="/app" className="active">
                Listings
              </NavLink>
            </li>
            <li>
              <NavLink to="/postjob" className="active">
                Post Jobs
              </NavLink>
            </li>
            <li>
              <NavLink to="/profile" className="active">
                Account
              </NavLink>
            </li>
          </ul>
        </div>
      </header>
    </nav>
  );
}

export default LandNav;

import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import './App.css';
import Activities from './components/Activities';
import Leaderboard from './components/Leaderboard';
import Teams from './components/Teams';
import Users from './components/Users';
import Workouts from './components/Workouts';

function App() {
  return (
    <Router>
      <div className="App">
        <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
          <div className="container-fluid">
            <Link className="navbar-brand" to="/">
              <img src="/octofit-logo.png" alt="OctoFit" className="navbar-logo" />
              OctoFit Tracker
            </Link>
            <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
              <span className="navbar-toggler-icon"></span>
            </button>
            <div className="collapse navbar-collapse" id="navbarNav">
              <ul className="navbar-nav">
                <li className="nav-item">
                  <Link className="nav-link" to="/users">Users</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/activities">Activities</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/teams">Teams</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/leaderboard">Leaderboard</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/workouts">Workouts</Link>
                </li>
              </ul>
            </div>
          </div>
        </nav>

        <Routes>
          <Route path="/" element={
            <div className="welcome-container">
              <div className="container">
                <h1 className="display-4">⚡ OCTOFIT HERO COMMAND CENTER ⚡</h1>
                <p className="lead hero-tagline">🦸 UNLEASH YOUR INNER SUPERHERO! TRAIN LIKE LEGENDS, COMPETE WITH TITANS! 🦸</p>
                <hr className="my-4 hero-divider" />
                <div className="row mt-5">
                  <div className="col-md-4 mb-4">
                    <Link to="/users" className="text-decoration-none">
                      <div className="card text-center h-100 shadow-sm hover-card hero-card">
                        <div className="card-body">
                          <div className="hero-icon">🦸‍♂️</div>
                          <h5 className="card-title mt-3">HEROES</h5>
                          <p className="card-text">Assemble Your Squad of Champions</p>
                        </div>
                      </div>
                    </Link>
                  </div>
                  <div className="col-md-4 mb-4">
                    <Link to="/activities" className="text-decoration-none">
                      <div className="card text-center h-100 shadow-sm hover-card hero-card">
                        <div className="card-body">
                          <div className="hero-icon">💪</div>
                          <h5 className="card-title mt-3">MISSIONS</h5>
                          <p className="card-text">Complete Epic Training Challenges</p>
                        </div>
                      </div>
                    </Link>
                  </div>
                  <div className="col-md-4 mb-4">
                    <Link to="/leaderboard" className="text-decoration-none">
                      <div className="card text-center h-100 shadow-sm hover-card hero-card">
                        <div className="card-body">
                          <div className="hero-icon">🏆</div>
                          <h5 className="card-title mt-3">HALL OF FAME</h5>
                          <p className="card-text">Battle for Ultimate Glory</p>
                        </div>
                      </div>
                    </Link>
                  </div>
                </div>
                <div className="row">
                  <div className="col-md-6 mb-4">
                    <Link to="/teams" className="text-decoration-none">
                      <div className="card text-center shadow-sm hover-card hero-card">
                        <div className="card-body">
                          <div className="hero-icon">🛡️</div>
                          <h5 className="card-title mt-3">LEAGUES</h5>
                          <p className="card-text">Form Your Superhero Alliance</p>
                        </div>
                      </div>
                    </Link>
                  </div>
                  <div className="col-md-6 mb-4">
                    <Link to="/workouts" className="text-decoration-none">
                      <div className="card text-center shadow-sm hover-card hero-card">
                        <div className="card-body">
                          <div className="hero-icon">⚡</div>
                          <h5 className="card-title mt-3">POWER TRAINING</h5>
                          <p className="card-text">Unlock Your Ultimate Potential</p>
                        </div>
                      </div>
                    </Link>
                  </div>
                </div>
              </div>
            </div>
          } />
          <Route path="/users" element={<Users />} />
          <Route path="/activities" element={<Activities />} />
          <Route path="/teams" element={<Teams />} />
          <Route path="/leaderboard" element={<Leaderboard />} />
          <Route path="/workouts" element={<Workouts />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;

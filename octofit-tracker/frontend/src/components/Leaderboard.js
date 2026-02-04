import React, { useState, useEffect } from 'react';

function Leaderboard() {
  const [leaderboard, setLeaderboard] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const API_URL = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/leaderboard/`;

  useEffect(() => {
    console.log('Leaderboard Component - Fetching from:', API_URL);
    
    fetch(API_URL)
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        console.log('Leaderboard Component - Raw data received:', data);
        // Handle both paginated (.results) and plain array responses
        const leaderboardData = data.results || data;
        console.log('Leaderboard Component - Processed data:', leaderboardData);
        setLeaderboard(Array.isArray(leaderboardData) ? leaderboardData : []);
        setLoading(false);
      })
      .catch(error => {
        console.error('Leaderboard Component - Error fetching data:', error);
        setError(error.message);
        setLoading(false);
      });
  }, [API_URL]);

  if (loading) return (
    <div className="container mt-4">
      <div className="loading-spinner">
        <div className="spinner-border text-primary" role="status">
          <span className="visually-hidden">Loading leaderboard...</span>
        </div>
      </div>
    </div>
  );
  
  if (error) return (
    <div className="container mt-4">
      <div className="alert alert-danger" role="alert">
        <h4 className="alert-heading">Error!</h4>
        <p>{error}</p>
      </div>
    </div>
  );

  return (
    <div className="container mt-4">
      <h2 className="mb-4">
        <i className="bi bi-trophy"></i> Leaderboard
      </h2>
      <div className="alert alert-info" role="alert">
        <i className="bi bi-info-circle"></i> Compete with others and climb to the top!
      </div>
      <div className="table-responsive">
        <table className="table table-striped table-hover">
          <thead>
            <tr>
              <th scope="col" style={{width: '10%'}}>Rank</th>
              <th scope="col">User</th>
              <th scope="col">Team</th>
              <th scope="col">Total Points</th>
              <th scope="col">Total Calories</th>
            </tr>
          </thead>
          <tbody>
            {leaderboard.length > 0 ? (
              leaderboard.map((entry, index) => (
                <tr key={entry.id || index} className={index < 3 ? 'table-warning' : ''}>
                  <td>
                    {index === 0 && <span className="badge bg-warning text-dark">🥇 {index + 1}</span>}
                    {index === 1 && <span className="badge bg-secondary">🥈 {index + 1}</span>}
                    {index === 2 && <span className="badge bg-danger">🥉 {index + 1}</span>}
                    {index > 2 && <span className="badge bg-light text-dark">{index + 1}</span>}
                  </td>
                  <td><strong>{entry.user_name || entry.user}</strong></td>
                  <td>
                    {entry.team_name || entry.team || <span className="text-muted">No Team</span>}
                  </td>
                  <td>
                    <span className="badge bg-success">{entry.total_points || 0} pts</span>
                  </td>
                  <td>{entry.total_calories || 0} cal</td>
                </tr>
              ))
            ) : (
              <tr>
                <td colSpan="5" className="text-center text-muted">
                  <em>No leaderboard data found</em>
                </td>
              </tr>
            )}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default Leaderboard;

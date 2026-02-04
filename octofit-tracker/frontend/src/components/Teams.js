import React, { useState, useEffect } from 'react';

function Teams() {
  const [teams, setTeams] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const API_URL = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/teams/`;

  useEffect(() => {
    console.log('Teams Component - Fetching from:', API_URL);
    
    fetch(API_URL)
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        console.log('Teams Component - Raw data received:', data);
        // Handle both paginated (.results) and plain array responses
        const teamsData = data.results || data;
        console.log('Teams Component - Processed data:', teamsData);
        setTeams(Array.isArray(teamsData) ? teamsData : []);
        setLoading(false);
      })
      .catch(error => {
        console.error('Teams Component - Error fetching data:', error);
        setError(error.message);
        setLoading(false);
      });
  }, [API_URL]);

  if (loading) return (
    <div className="container mt-4">
      <div className="loading-spinner">
        <div className="spinner-border text-primary" role="status">
          <span className="visually-hidden">Loading teams...</span>
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
        <i className="bi bi-people"></i> Teams
      </h2>
      <div className="d-flex justify-content-between align-items-center mb-3">
        <p className="text-muted mb-0">Total Teams: <strong>{teams.length}</strong></p>
        <button className="btn btn-success">
          <i className="bi bi-plus-circle"></i> Create New Team
        </button>
      </div>
      <div className="row">
        {teams.length > 0 ? (
          teams.map((team) => (
            <div key={team.id} className="col-md-4 mb-4">
              <div className="card h-100">
                <div className="card-body d-flex flex-column">
                  <h5 className="card-title">
                    <i className="bi bi-flag"></i> {team.name}
                  </h5>
                  <p className="card-text flex-grow-1">
                    {team.description || <em className="text-muted">No description available</em>}
                  </p>
                  <div className="mt-auto">
                    {team.member_count && (
                      <p className="card-text mb-2">
                        <span className="badge bg-primary">
                          <i className="bi bi-person"></i> {team.member_count} Members
                        </span>
                      </p>
                    )}
                    <p className="card-text">
                      <small className="text-muted">
                        <i className="bi bi-calendar"></i> Created: {new Date(team.created_at).toLocaleDateString()}
                      </small>
                    </p>
                    <button className="btn btn-outline-primary btn-sm w-100">
                      View Details
                    </button>
                  </div>
                </div>
              </div>
            </div>
          ))
        ) : (
          <div className="col-12">
            <div className="alert alert-info text-center" role="alert">
              <i className="bi bi-info-circle"></i> No teams found. Create one to get started!
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default Teams;

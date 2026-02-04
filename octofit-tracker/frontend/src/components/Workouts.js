import React, { useState, useEffect } from 'react';

function Workouts() {
  const [workouts, setWorkouts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const API_URL = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/workouts/`;

  useEffect(() => {
    console.log('Workouts Component - Fetching from:', API_URL);
    
    fetch(API_URL)
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        console.log('Workouts Component - Raw data received:', data);
        // Handle both paginated (.results) and plain array responses
        const workoutsData = data.results || data;
        console.log('Workouts Component - Processed data:', workoutsData);
        setWorkouts(Array.isArray(workoutsData) ? workoutsData : []);
        setLoading(false);
      })
      .catch(error => {
        console.error('Workouts Component - Error fetching data:', error);
        setError(error.message);
        setLoading(false);
      });
  }, [API_URL]);

  if (loading) return (
    <div className="container mt-4">
      <div className="loading-spinner">
        <div className="spinner-border text-primary" role="status">
          <span className="visually-hidden">Loading workouts...</span>
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
        <i className="bi bi-lightning"></i> Personalized Workouts
      </h2>
      <div className="alert alert-success" role="alert">
        <i className="bi bi-check-circle"></i> These workouts are tailored to help you reach your fitness goals!
      </div>
      <div className="d-flex justify-content-between align-items-center mb-3">
        <p className="text-muted mb-0">Available Workouts: <strong>{workouts.length}</strong></p>
        <button className="btn btn-primary">
          <i className="bi bi-filter"></i> Filter Workouts
        </button>
      </div>
      <div className="row">
        {workouts.length > 0 ? (
          workouts.map((workout) => (
            <div key={workout.id} className="col-md-6 mb-4">
              <div className="card h-100">
                <div className="card-body d-flex flex-column">
                  <h5 className="card-title">
                    <i className="bi bi-clipboard-check"></i> {workout.name}
                  </h5>
                  <p className="card-text flex-grow-1">
                    {workout.description || <em className="text-muted">No description available</em>}
                  </p>
                  <ul className="list-group list-group-flush mb-3">
                    {workout.difficulty && (
                      <li className="list-group-item">
                        <strong><i className="bi bi-speedometer"></i> Difficulty:</strong>{' '}
                        <span className={`badge ${
                          workout.difficulty.toLowerCase() === 'easy' ? 'bg-success' :
                          workout.difficulty.toLowerCase() === 'medium' ? 'bg-warning text-dark' :
                          'bg-danger'
                        }`}>
                          {workout.difficulty}
                        </span>
                      </li>
                    )}
                    {workout.duration && (
                      <li className="list-group-item">
                        <strong><i className="bi bi-clock"></i> Duration:</strong> {workout.duration} minutes
                      </li>
                    )}
                    {workout.category && (
                      <li className="list-group-item">
                        <strong><i className="bi bi-tag"></i> Category:</strong>{' '}
                        <span className="badge bg-info">{workout.category}</span>
                      </li>
                    )}
                    {workout.target_calories && (
                      <li className="list-group-item">
                        <strong><i className="bi bi-fire"></i> Target Calories:</strong> {workout.target_calories}
                      </li>
                    )}
                  </ul>
                  <div className="mt-auto">
                    <button className="btn btn-primary w-100">
                      <i className="bi bi-play-circle"></i> Start Workout
                    </button>
                  </div>
                </div>
              </div>
            </div>
          ))
        ) : (
          <div className="col-12">
            <div className="alert alert-info text-center" role="alert">
              <i className="bi bi-info-circle"></i> No workouts found. Check back later for personalized recommendations!
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default Workouts;

import React, { useState, useEffect } from 'react';

function Users() {
  const [users, setUsers] = useState([]);
  const [teams, setTeams] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [editingUser, setEditingUser] = useState(null);
  const [showModal, setShowModal] = useState(false);
  const [formData, setFormData] = useState({
    name: '',
    username: '',
    email: '',
    team_id: ''
  });

  const API_URL = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/users/`;
  const TEAMS_API_URL = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/teams/`;

  useEffect(() => {
    console.log('Users Component - Fetching from:', API_URL);
    
    // Fetch users and teams
    Promise.all([
      fetch(API_URL).then(r => r.json()),
      fetch(TEAMS_API_URL).then(r => r.json())
    ])
      .then(([usersData, teamsData]) => {
        console.log('Users Component - Raw data received:', usersData);
        const users = usersData.results || usersData;
        const teams = teamsData.results || teamsData;
        
        setUsers(Array.isArray(users) ? users : []);
        setTeams(Array.isArray(teams) ? teams : []);
        setLoading(false);
      })
      .catch(error => {
        console.error('Users Component - Error fetching data:', error);
        setError(error.message);
        setLoading(false);
      });
  }, [API_URL, TEAMS_API_URL]);

  const handleEdit = (user) => {
    setEditingUser(user);
    setFormData({
      name: user.name || '',
      username: user.username || '',
      email: user.email || '',
      team_id: user.team_id || ''
    });
    setShowModal(true);
  };

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    try {
      const response = await fetch(`${API_URL}${editingUser.id}/`, {
        method: 'PATCH',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData)
      });

      if (!response.ok) {
        throw new Error('Failed to update user');
      }

      const updatedUser = await response.json();
      
      // Update the users list
      setUsers(users.map(u => u.id === updatedUser.id ? updatedUser : u));
      setShowModal(false);
      setEditingUser(null);
    } catch (error) {
      console.error('Error updating user:', error);
      alert('Failed to update user. Please try again.');
    }
  };

  const handleClose = () => {
    setShowModal(false);
    setEditingUser(null);
    setFormData({ name: '', username: '', email: '', team_id: '' });
  };

  if (loading) return (
    <div className="container mt-4">
      <div className="loading-spinner">
        <div className="spinner-border text-primary" role="status">
          <span className="visually-hidden">Loading users...</span>
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
        <i className="bi bi-person-circle"></i> Users
      </h2>
      <div className="d-flex justify-content-between align-items-center mb-3">
        <p className="text-muted mb-0">Total Users: <strong>{users.length}</strong></p>
        <button className="btn btn-primary">
          <i className="bi bi-person-plus"></i> Add New User
        </button>
      </div>
      <div className="table-responsive">
        <table className="table table-striped table-hover">
          <thead>
            <tr>
              <th scope="col">Name</th>
              <th scope="col">Username</th>
              <th scope="col">Email</th>
              <th scope="col">Team</th>
              <th scope="col">Joined</th>
              <th scope="col">Actions</th>
            </tr>
          </thead>
          <tbody>
            {users.length > 0 ? (
              users.map((user) => (
                <tr key={user.id}>
                  <td>
                    <strong><i className="bi bi-person-fill"></i> {user.name || 'N/A'}</strong>
                  </td>
                  <td>
                    <span className="text-primary">@{user.username || user.email.split('@')[0]}</span>
                  </td>
                  <td>
                    <a href={`mailto:${user.email}`} className="text-decoration-none">
                      <i className="bi bi-envelope"></i> {user.email}
                    </a>
                  </td>
                  <td>
                    {user.team_name || user.team ? (
                      <span className="badge bg-info">{user.team_name || user.team}</span>
                    ) : (
                      <span className="text-muted">No Team</span>
                    )}
                  </td>
                  <td>
                    <small className="text-muted">
                      {new Date(user.created_at || user.date_joined).toLocaleDateString()}
                    </small>
                  </td>
                  <td>
                    <button 
                      className="btn btn-sm btn-outline-primary"
                      onClick={() => handleEdit(user)}
                    >
                      <i className="bi bi-pencil"></i> Edit
                    </button>
                  </td>
                </tr>
              ))
            ) : (
              <tr>
                <td colSpan="6" className="text-center text-muted">
                  <em>No users found</em>
                </td>
              </tr>
            )}
          </tbody>
        </table>
      </div>

      {/* Edit User Modal */}
      {showModal && (
        <div className="modal fade show" style={{ display: 'block', backgroundColor: 'rgba(0,0,0,0.5)' }}>
          <div className="modal-dialog modal-dialog-centered">
            <div className="modal-content">
              <div className="modal-header">
                <h5 className="modal-title">
                  <i className="bi bi-pencil-square"></i> Edit User
                </h5>
                <button type="button" className="btn-close" onClick={handleClose}></button>
              </div>
              <form onSubmit={handleSubmit}>
                <div className="modal-body">
                  <div className="mb-3">
                    <label htmlFor="name" className="form-label">Name</label>
                    <input
                      type="text"
                      className="form-control"
                      id="name"
                      name="name"
                      value={formData.name}
                      onChange={handleInputChange}
                      required
                    />
                  </div>
                  <div className="mb-3">
                    <label htmlFor="username" className="form-label">Username</label>
                    <input
                      type="text"
                      className="form-control"
                      id="username"
                      name="username"
                      value={formData.username}
                      onChange={handleInputChange}
                    />
                  </div>
                  <div className="mb-3">
                    <label htmlFor="email" className="form-label">Email</label>
                    <input
                      type="email"
                      className="form-control"
                      id="email"
                      name="email"
                      value={formData.email}
                      onChange={handleInputChange}
                      required
                    />
                  </div>
                  <div className="mb-3">
                    <label htmlFor="team_id" className="form-label">Team</label>
                    <select
                      className="form-select"
                      id="team_id"
                      name="team_id"
                      value={formData.team_id}
                      onChange={handleInputChange}
                    >
                      <option value="">No Team</option>
                      {teams.map(team => (
                        <option key={team.id} value={team.id}>
                          {team.name}
                        </option>
                      ))}
                    </select>
                  </div>
                </div>
                <div className="modal-footer">
                  <button type="button" className="btn btn-secondary" onClick={handleClose}>
                    Cancel
                  </button>
                  <button type="submit" className="btn btn-primary">
                    <i className="bi bi-save"></i> Save Changes
                  </button>
                </div>
              </form>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

export default Users;

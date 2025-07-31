import { useState, useEffect } from 'react';
import { useParams, Link } from 'react-router-dom';
import api from '../../services/api';

const BeneficiaryStories = () => {
    const { beneficiaryId } = useParams();
    const [stories, setStories] = useState([]);
    const [title, setTitle] = useState('');
    const [content, setContent] = useState('');

    useEffect(() => {
        const fetchStories = async () => {
            try {
                const response = await api.get(`/beneficiaries/${beneficiaryId}/stories`);
                setStories(response.data);
            } catch (error) {
                console.error('Error fetching stories:', error);
            }
        };
        fetchStories();
    }, [beneficiaryId]);

    const handleCreateStory = async (e) => {
        e.preventDefault();
        try {
            await api.post(`/beneficiaries/${beneficiaryId}/stories`, { title, content });
            setTitle('');
            setContent('');
            const response = await api.get(`/beneficiaries/${beneficiaryId}/stories`);
            setStories(response.data);
        } catch (error) {
            console.error('Error creating story:', error);
        }
    };

    const handleDeleteStory = async (storyId) => {
        try {
            await api.delete(`/beneficiaries/${beneficiaryId}/stories/${storyId}`);
            const response = await api.get(`/beneficiaries/${beneficiaryId}/stories`);
            setStories(response.data);
        } catch (error) {
            console.error('Error deleting story:', error);
        }
    };

    return (
        <div className="container mt-4">
            <h2>Beneficiary Stories</h2>
            <form onSubmit={handleCreateStory} className="mb-4">
                <div className="mb-3">
                    <label htmlFor="title" className="form-label">Title</label>
                    <input type="text" className="form-control" id="title" value={title} onChange={(e) => setTitle(e.target.value)} required />
                </div>
                <div className="mb-3">
                    <label htmlFor="content" className="form-label">Content</label>
                    <textarea className="form-control" id="content" rows="3" value={content} onChange={(e) => setContent(e.target.value)} required></textarea>
                </div>
                <button type="submit" className="btn btn-primary">Create Story</button>
            </form>
            <ul className="list-group">
                {stories.map(story => (
                    <li key={story.id} className="list-group-item d-flex justify-content-between align-items-center">
                        <div>
                            <h5>{story.title}</h5>
                            <p>{story.content}</p>
                            <small className="text-muted">{new Date(story.created_at).toLocaleString()}</small>
                        </div>
                        <button className="btn btn-danger" onClick={() => handleDeleteStory(story.id)}>Delete</button>
                    </li>
                ))}
            </ul>
            <Link to={`/donor/organizations`} className="btn btn-secondary mt-3">Back to Organizations</Link>
        </div>
    );
};

export default BeneficiaryStories;

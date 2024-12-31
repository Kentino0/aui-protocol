import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [uiSpec, setUiSpec] = useState(null);

  useEffect(() => {
    axios.get("http://localhost:8001/context/user123")
      .then(res => axios.post("http://localhost:8002/ui/generate", res.data))
      .then(uiRes => {
        setUiSpec(uiRes.data);
      })
      .catch(err => console.error(err));
  }, []);

  const handleFeedback = (label) => {
    axios.post("http://localhost:8003/feedback/log", {
      eventType: "button_click",
      label
    }).catch(err => console.error(err));
  };

  const renderComponent = (comp, idx) => {
    switch (comp.type) {
      case 'text':
        return <p key={idx}>{comp.props.content}</p>;
      case 'button':
        return (
          <button key={idx} onClick={() => handleFeedback(comp.props.label)}>
            {comp.props.label}
          </button>
        );
      case 'badge':
        return <span key={idx} style={{ marginLeft: '8px' }}>{comp.props.label}</span>;
      default:
        return null;
    }
  };

  const renderLayout = (layout) => {
    if (!layout) return null;
    const direction = (layout.type === 'vertical-stack') ? 'column' : 'row';
    return (
      <div style={{ display: 'flex', flexDirection: direction, gap: '1rem' }}>
        {layout.children.map((child, idx) => renderComponent(child, idx))}
      </div>
    );
  };

  return (
    <div style={{ padding: '20px' }}>
      <h1>AUI Protocol Demo</h1>
      {uiSpec ? renderLayout(uiSpec.layout) : <p>Loading UI...</p>}
    </div>
  );
}

export default App;

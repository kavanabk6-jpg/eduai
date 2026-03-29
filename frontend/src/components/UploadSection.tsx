import React, { useState } from 'react';

const UploadSection: React.FC = () => {
    const [file, setFile] = useState<File | null>(null);

    const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        const selectedFile = event.target.files![0];
        setFile(selectedFile);
    };

    const handleUpload = async () => {
        if (!file) return;
        // File upload logic goes here
        console.log('Uploading:', file.name);
        // Placeholder: Implement actual upload functionality
    };

    return (
        <div>
            <h2>Upload Section</h2>
            <input type="file" onChange={handleFileChange} />
            <button onClick={handleUpload}>Upload</button>
        </div>
    );
};

export default UploadSection;
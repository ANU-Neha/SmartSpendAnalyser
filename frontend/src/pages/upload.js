import { useState } from 'react';
import Layout from '../components/Layout';
import { Button, Paper, Typography, Box, CircularProgress } from '@mui/material';
import { CloudUpload } from '@mui/icons-material';
import { uploadReceipt } from '../utils/api'; // Add this import

export default function Upload() {
    const [isUploading, setIsUploading] = useState(false);
    const [uploadSuccess, setUploadSuccess] = useState(false);
    const [file, setFile] = useState(null); // Add file state

    const handleUpload = async (e) => {
        e.preventDefault();
        if (!file) {
            alert("Please select an image to upload."); // User feedback
            return;
        }

        setIsUploading(true);

        try {
            // Replace 'current_user_id' with a dynamic value if you implement authentication
            await uploadReceipt(file, 'user_kagle');
            setUploadSuccess(true);
            setFile(null); // Clear the selected file after successful upload
            // Optional: You might want to redirect the user or update a list of receipts here
            setTimeout(() => setUploadSuccess(false), 3000);
        } catch (error) {
            console.error('Upload failed:', error);
            alert('Upload failed. Please try again.'); // User feedback on failure
        } finally {
            setIsUploading(false);
        }
    };

    return (
        <Layout>
        <Typography variant="h4" gutterBottom>
            Upload Receipt
        </Typography>

        <Paper sx={{ p: 3 }}>
            <Typography variant="body1" paragraph>
            Upload your receipt image to automatically track your spending.
            </Typography>

            <Box
                component="form"
                onSubmit={handleUpload}
                sx={{
                    display: 'flex',
                    flexDirection: 'column',
                    alignItems: 'center',
                    mt: 3,
                }}
            >
                <Button
                    variant="contained"
                    component="label"
                    startIcon={<CloudUpload />}
                    disabled={isUploading}
                >
                    Select Image
                    <input
                        type="file"
                        hidden
                        accept="image/*"
                        onChange={(e) => setFile(e.target.files[0])} // Set file state
                    />
                </Button>

                {file && (
                    <Typography variant="body2" sx={{ mt: 1 }}>
                        Selected file: {file.name}
                    </Typography>
                )}

                {isUploading ? (
                    <Box sx={{ display: 'flex', alignItems: 'center', mt: 2 }}>
                        <CircularProgress size={24} sx={{ mr: 2 }} />
                        <Typography>Processing receipt...</Typography>
                    </Box>
                ) : uploadSuccess ? (
                    <Typography color="primary" sx={{ mt: 2 }}>
                        Receipt processed successfully!
                    </Typography>
                ) : (
                    <Button
                        type="submit"
                        variant="contained"
                        color="primary"
                        sx={{ mt: 2 }}
                        disabled={isUploading || !file} // Disable if no file selected
                    >
                        Upload Receipt
                    </Button>
                )}
            </Box>
        </Paper>
        </Layout>
    );
}
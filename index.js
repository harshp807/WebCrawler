const axios = require('axios');

// Function to print the sitemap in a tree-like structure
function printSitemap(sitemap, url, level = 0) {
    if (!sitemap[url]) return;

    const indentation = ' '.repeat(level * 2);
    console.log(`${indentation}- ${url}`);

    sitemap[url].forEach(link => {
        printSitemap(sitemap, link, level + 1);  // Recursive call to print nested links
    });
}

// Function to fetch the sitemap from the server
async function fetchSitemap(url) {
    try {
        const response = await axios.post('http://127.0.0.1:5000/crawl', { url: url });
        const sitemap = response.data;

        console.log('Sitemap:');
        printSitemap(sitemap, url);
    } catch (error) {
        console.error('Error fetching sitemap:', error.message);
    }
}

// Main function to run the client
const url = process.argv[2] || 'https://www.redhat.com';  // Default URL if none provided
fetchSitemap(url);

"""File downloader module"""
import os
import random
import requests
from typing import Optional, BinaryIO, Dict
from urllib.parse import urlparse

class FileDownloader:
    """File downloader class"""
    
    # Common User-Agent list
    USER_AGENTS = [
        # Windows Chrome
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
        
        # Mac Chrome
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
        
        # Windows Edge
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/120.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/119.0.0.0 Safari/537.36',
        
        # Windows Firefox
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0',
        
        # Mac Safari
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Safari/605.1.15',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Safari/605.1.15',
        
        # Mac Firefox
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:121.0) Gecko/20100101 Firefox/121.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:120.0) Gecko/20100101 Firefox/120.0',
        
        # Mobile Chrome
        'Mozilla/5.0 (iPhone; CPU iPhone OS 17_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/120.0.6099.119 Mobile/15E148 Safari/604.1',
        'Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.210 Mobile Safari/537.36',
        
        # Mobile Safari
        'Mozilla/5.0 (iPhone; CPU iPhone OS 17_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Mobile/15E148 Safari/604.1',
    ]
    
    @classmethod
    def _get_random_user_agent(cls) -> str:
        """Get a random User-Agent string"""
        return random.choice(cls.USER_AGENTS)
    
    @classmethod
    def get_stream(
        cls,
        url: str,
        referer: Optional[str] = None,
        headers: Optional[Dict[str, str]] = None,
        timeout: int = 30
    ) -> BinaryIO:
        """
        Get file stream from URL
        
        Args:
            url: File URL to download
            referer: Referer URL (optional)
            headers: Additional headers (optional)
            timeout: Request timeout in seconds
            
        Returns:
            BinaryIO: File stream object
            
        Raises:
            requests.exceptions.RequestException: When download fails
            
        Examples:
            >>> stream = FileDownloader.get_stream('https://example.com/file.pdf')
            >>> with open('file.pdf', 'wb') as f:
            ...     f.write(stream.read())
        """
        # Initialize headers
        request_headers = headers or {}
        
        # Add random User-Agent if not present
        if 'User-Agent' not in request_headers:
            request_headers['User-Agent'] = cls._get_random_user_agent()
            
        # Add referer if provided
        if referer:
            request_headers['Referer'] = referer
            
        # Make request with stream=True
        response = requests.get(
            url,
            headers=request_headers,
            stream=True,
            timeout=timeout
        )
        response.raise_for_status()
        
        return response.raw
    
    @classmethod
    def download_file(
        cls,
        url: str,
        output_path: Optional[str] = None,
        referer: Optional[str] = None,
        headers: Optional[Dict[str, str]] = None,
        timeout: int = 30,
        chunk_size: int = 8192
    ) -> str:
        """
        Download file from URL to local path
        
        Args:
            url: File URL to download
            output_path: Local path to save file (optional)
            referer: Referer URL (optional)
            headers: Additional headers (optional)
            timeout: Request timeout in seconds
            chunk_size: Size of chunks to download
            
        Returns:
            str: Path to downloaded file
            
        Examples:
            >>> path = FileDownloader.download_file('https://example.com/file.pdf')
            >>> print(f'Downloaded to: {path}')
        """
        # Get file name from URL if output_path not provided
        if not output_path:
            file_name = os.path.basename(urlparse(url).path)
            if not file_name:
                file_name = 'downloaded_file'
            output_path = file_name
            
        # Get file stream
        stream = cls.get_stream(
            url,
            referer=referer,
            headers=headers,
            timeout=timeout
        )
        
        # Download file in chunks
        with open(output_path, 'wb') as f:
            while True:
                chunk = stream.read(chunk_size)
                if not chunk:
                    break
                f.write(chunk)
                
        return output_path 
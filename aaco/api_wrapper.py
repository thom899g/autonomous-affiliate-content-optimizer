"""
 API Wrapper Module for AACO
 Handles deployment of content through various APIs.
"""

from typing import Dict, Any
import logging
import requests

logger = logging.getLogger(__name__)

def deploy_content(content: str, config: Dict[str, Any]) -> bool:
    """
    Deploys generated content to target platforms via APIs.
    Args:
        content: Generated content to deploy.
        config: Configuration parameters for deployment.
    Returns:
        Boolean indicating success of deployment.
    """
    try:
        # Example API call
        response = requests.post(
            url=config['api_url'],
            json={'content': content, 'platform_id': config['platform_id']},
            headers={'Authorization': config['api_key']}
        )

        if response.status_code == 200:
            logger.info(f"Content deployed successfully to platform {config['platform_id']}")
            return True
        else:
            raise Exception(f"Deployment failed with status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        logger.error(f"API request failed: {str(e)}")
        raise
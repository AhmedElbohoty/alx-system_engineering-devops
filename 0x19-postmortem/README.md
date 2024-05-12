## Issue Summary:

For hour and half at May 11, 2024, 08:00 UTC to May 11, 2024, 12:00 UTC, our Apache service outage resulting in a 500 error; 100% of users experienced service error.

## Timeline:

08:00 UTC: HTTP 500 error is detected through monitoring alerts.

08:10 UTC: Investigation initiated by the web team.

08:30 UTC: Initial assumption was that the issue may be related to Apache upgrade.

09:00 UTC: Further investigation reveals a configurations error in wp-settings.php.

9:30 UTC: Issue resolved by correcting the configurations.

## Root Cause and Resolution:

The root cause of the 500 error was a misconfiguration in the wp-settings.php file.

An incorrect reference to a PHP module was introduced, leading to the error.

This issue was resolved by manually editing the wp-settings.php file on the server to correct the erroneous reference.

## Corrective and Preventative Measures:

1- Update server configuration documentation.

2- Regular review of server configurations.

3- Implement automated configuration management using Puppet to ensure consistency.

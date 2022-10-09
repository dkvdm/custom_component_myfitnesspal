# ATTENTION
MyFitnesspal has change their login so this component does not work anymore. At this time there are no solution until the underlying scraping API used is updated.
Sorry for the inconvenience.

# Myfitnesspal custom component
This custom component gets fitness data from your account. Please note that the component uses an underlying scraping API that can change at any time and use at your own risk. **The author takes no liability of usage**.

# Usage

## Configuration
The API login with username/password has stopped working, so we have to use cookie session data instead.

Run the following command on you local machine:
`python cookiejar_generate.py`

This should generate `myfitnesspal_cookiejar.pkl` which you should copy to `custom_components/my_fitnesspal/myfitnesspal_cookiejar.pkl`


## Copy and paste
*If you use HACS, skip this step!*
The component can be used by copying everything under the `custom_component` folder to your `custom_component`, i.e. the `my_fitnesspal` folder.

### Configure through integrations (prefered way)
Check under configuration/integrations. Add the `Myfitnesspal` integration.

### Configure with old school yaml
Not supported

### Configuration properties
|property|description|
|---|---|
|name|Name of sensor
|username|Your user name at myfitnesspal
|password|Your password at myfitnesspal
|   |   |


## HACS component
*THIS COMPONENT IS REMOVED FROM HACS UNITL FURTHER NOTICE.*


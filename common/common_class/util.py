'''
 # @ Author: Tanmay Anthony Gomes
 # @ Create Time: 2025-06-12 15:13:41
 # @ Modified by: Tanmay Anthony Gomes
 # @ Modified time: 2025-06-12 17:49:03
 # @ Description: response function for returning result. will be called from DAL classes
 '''
def _response(status, message, data=None):
    return {
        "status": status,
        "message": message,
        "data": data or []
    }

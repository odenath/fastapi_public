# import schedule
# import time
# from crud import update_data
# from database import get_source_session, get_destination_session

# def job():
#     update_data(get_source_session, get_destination_session)
    
    
# schedule.every().day.at("00:00").do(job)
# while True:
#     schedule.run_pending()
#     time.sleep(1)
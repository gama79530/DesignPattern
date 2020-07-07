import Observer
import Subject

if __name__ == "__main__" :
    weather_data = Subject.WeatherData()
    current_display = Observer.CurrentConditionsDisplay()
    statistics_display = Observer.StatisticsDisplay()
    forecast_display = Observer.ForecastDisplay()

    print('---- Push mode ----')
    weather_data.registerPushObserver(current_display)
    weather_data.registerPushObserver(statistics_display)
    weather_data.registerPushObserver(forecast_display)

    weather_data.simulateChange(80, 65, 30.4)
    weather_data.simulateChange(82, 70, 29.2)
    weather_data.simulateChange(78, 90, 29.2)

    weather_data.removePushObserver(current_display)
    weather_data.removePushObserver(statistics_display)
    weather_data.removePushObserver(forecast_display)
    print('---- Pull mode ----')    
    weather_data.registerPullObserver(current_display)
    weather_data.registerPullObserver(statistics_display)
    weather_data.registerPullObserver(forecast_display)

    weather_data.simulateChange(80, 65, 30.4)
    weather_data.simulateChange(82, 70, 29.2)
    weather_data.simulateChange(78, 90, 29.2)

    weather_data.removePullObserver(current_display)
    weather_data.removePullObserver(statistics_display)
    weather_data.removePullObserver(forecast_display)
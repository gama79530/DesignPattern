import Observer
import Subject

if __name__ == "__main__" :
    print('---- push mode ----')
    weather_data = Subject.WeatherData()
    current_display = Observer.CurrentConditionsDisplay(weather_data)
    statistics_display = Observer.StatisticsDisplay(weather_data)
    forecast_display = Observer.ForecastDisplay(weather_data)


    weather_data.simulateChange(80, 65, 30.4)
    weather_data.simulateChange(82, 70, 29.2)
    weather_data.simulateChange(78, 90, 29.2)
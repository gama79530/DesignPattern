# Observer Pattern (Behavioral, Object)

## Example description
1. **WeatherData** object maintains 3 values, _temperature, humidity and pressure_. And it has to notify all registered Display object whenever these 3 value change.
1. Each **Display** object gets these 3 values from WeatherData object and display their info according  to these values.

## Comment
1. One Subject,many observers.
1. Subject have to notify all registered observer whenever specific event (which is often GUI event or value change event) happens.
1. **"Subject push data to observer"** means subject decide how to structure data and pass them to observers when _update_.
1. **"Observer pull data from subject"** means subject pass its reference to observer when _update_ and observer use this reference to get data from subject.

## Summary
1. **The Observer Pattern** defines a one-to-many dependency between objects so that when one object changes state, all of its dependents are notified and updated automatically.
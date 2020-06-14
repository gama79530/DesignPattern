import Invoker
import ThirdParty.Light.Light
import ThirdParty.Light.LightCommand
import ThirdParty.Fan.CeilingFan
import ThirdParty.Fan.FanCommand

if __name__ == "__main__":
    remote_control = Invoker.RemoteControlWithUndo()
    
    living_room_light = ThirdParty.Light.Light.Light('Living Room')
    living_room_light_on = ThirdParty.Light.LightCommand.LightOnCommand(living_room_light)
    living_room_light_off = ThirdParty.Light.LightCommand.LightOffCommand(living_room_light)

    remote_control.setCommand(0, living_room_light_on, living_room_light_off)

    remote_control.onButtonWasPushed(0)
    remote_control.offButtonWasPushed(0)
    print(str(remote_control))
    remote_control.undoButtonWasPushed()

    remote_control.offButtonWasPushed(0)
    remote_control.onButtonWasPushed(0)
    print(str(remote_control))
    remote_control.undoButtonWasPushed()

    ceiling_fan = ThirdParty.Fan.CeilingFan.CeilingFan('Living Room')

    ceiling_fan_medium = ThirdParty.Fan.FanCommand.CeilingFanMediumCommand(ceiling_fan)
    ceiling_fan_high = ThirdParty.Fan.FanCommand.CeilingFanHighCommand(ceiling_fan)
    ceiling_fan_off = ThirdParty.Fan.FanCommand.CeilingFanOffCommand(ceiling_fan)

    remote_control.setCommand(0, ceiling_fan_medium, ceiling_fan_off)
    remote_control.setCommand(1, ceiling_fan_high, ceiling_fan_off)

    remote_control.onButtonWasPushed(0)
    remote_control.offButtonWasPushed(0)
    print(str(remote_control))
    remote_control.undoButtonWasPushed()

    remote_control.onButtonWasPushed(1)
    print(str(remote_control))
    remote_control.undoButtonWasPushed()
import cec

from fauxmo.plugins import FauxmoPlugin

cec.init()
stereo = cec.Device(CECDEVICE_AUDIOSYSTEM)
broadcast = cec.Device(CECDEVICE_BROADCAST)


class cecplugin(FauxmoPlugin):

    def __init__(self, name: str, port: int, on_cmd: str, off_cmd: str,
                 state_cmd: str = None) -> None:


        self.on_cmd = on_cmd
        self.off_cmd = off_cmd
        self.state_cmd = state_cmd

        super().__init__(name=name, port=port)

    def run_cmd(self, cmd: str) -> bool:
        """Partialmethod to run command.
        Args:
            cmd: Command to be run
        Returns:
            True if command seems to have run without error
        """
        cmds = cmd.split(",")
        for i in cmds:
            cecdevice.transmit(i)

        return true

    def on(self):
        """Run on command.
        Returns:
            True if command seems to have run without error.
        """
        if self.on_cmd == "stereo":
            stereo.power_on()
            stereo.transmit(CEC_OPCODE_SYSTEM_AUDIO_MODE_REQUEST, bytes([0x00, 0x00]))
        if self.on_cmd == "airplay":
            broadcast.transmit(CEC_OPCODE_ACTIVE_SOURCE, bytes([0x10, 0x00]))

        return true

    def off(self):
        """Run off command.
        Returns:
            True if command seems to have run without error.
        """
        if self.on_cmd == "stereo":
            stereo.standby()
        if self.on_cmd == "airplay":
            broadcast.transmit(CEC_OPCODE_ACTIVE_SOURCE, bytes([0x20, 0x00]))
        return true

    def get_state(self) -> str:
        """Get device state.
        NB: Return code of `0` (i.e. ran without error) indicates "on" state,
        otherwise will be off. making it easier to have something like `ls
        path/to/pidfile` suggest `on`. Many command line switches may not
        actually have a "state" per se (just an arbitary command you want to
        run), in which case you could just put "false" as the command, which
        should always return "off".
        Returns:
            "on" or "off" if `state_cmd` is defined, "unknown" if undefined
        """

        return "unknown"

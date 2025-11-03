/**
 * @author: Charan Abburu & Jasraj Bhatia
 * Team 4099 Manipulator IO Practice
 */

object ManipulatorIONeo : ManipulatorIO {

    private val rampRateSeconds = 1

    private val leaderSparkMax =
        CANSparkMax(Constants.Manipulator.LEADER_MOTOR_ID, CANSparkMaxLowLevel.MotorType.kBrushless)

    private val leaderSensor =
        sparkMaxLinearMechanismSensor(
            leaderSparkMax,
            ManipulatorConstants.MANIPULATOR_PULLEY_TO_MOTOR,
            ManipulatorConstants.SPOOL_DIAMETER,
            ManipulatorConstants.VOLTAGE_COMPENSATION
        )

    private val followerSparkMax =
        CANSparkMax(Constants.Manipulator.FOLLOWER_MOTOR_ID, CANSparkMaxLowLevel.MotorType.kBrushless)

    private val followerSensor =
        sparkMaxLinearMechanismSensor(
            followerSparkMax,
            ManipulatorConstants.MANIPULATOR_PULLEY_TO_MOTOR,
            ManipulatorConstants.SPOOL_DIAMETER,
            ManipulatorConstants.VOLTAGE_COMPENSATION
        )

    private val leaderPIDController: SparkMaxPIDController = leaderSparkMax.pidController
    private val followerPIDController: SparkMaxPIDController = followerSparkMax.pidController

    init {
        // Reset motor settings to factory defaults
        leaderSparkMax.restoreFactoryDefaults() 
        followerSparkMax.restoreFactoryDefaults()

        // Clear any faults
        leaderSparkMax.clearFaults()
        followerSparkMax.clearFaults()

        // Basic settings
        leaderSparkMax.enableVoltageCompensation(ManipulatorConstants.VOLTAGE_COMPENSATION.inVolts)
        followerSparkMax.enableVoltageCompensation(ManipulatorConstants.VOLTAGE_COMPENSATION.inVolts)

        leaderSparkMax.inverted = ManipulatorConstants.LEADER_INVERTED

        leaderSparkMax.setSmartCurrentLimit(
            ManipulatorConstants.LEADER_STATOR_CURRENT_LIMIT.inAmperes.toInt()
        )
        followerSparkMax.setSmartCurrentLimit(
            ManipulatorConstants.FOLLOWER_STATOR_CURRENT_LIMIT.inAmperes.toInt()
        )


        leaderSparkMax.idleMode = CANSparkMax.IdleMode.kBrake
        followerSparkMax.idleMode = CANSparkMax.IdleMode.kBrake

        // Make follower motor mirror the leader
        followerSparkMax.follow(leaderSparkMax, ManipulatorConstants.FOLLOWER_INVERTED) 

        leaderPIDController.ff = 0.0

        // Burn flash memory
        leaderSparkMax.burnFlash()
        followerSparkMax.burnFlash()

        // Add motors to the motor checker
        MotorChecker.add(
            "Manipulator",
            "Extension",
            MotorCollection(
                mutableListOf(
                    Neo(leaderSparkMax, "Leader Extension Motor"),
                    Neo(followerSparkMax, "Follower Extension Motor")
                ),
                ManipulatorConstants.LEADER_STATOR_CURRENT_LIMIT,
                30.celsius,
                ManipulatorConstants.LEADER_STATOR_CURRENT_LIMIT - 10.amps,
                80.celsius
            ),
        )
        leaderSparkMax.setOpenLoopRampRate(rampRateSeconds)
    }

    override fun updateInputs(inputs: ManipulatorIO.ManipulatorInputs) {
        inputs.manipulatorPosition = leaderSensor.position

        inputs.manipulatorVelocity = leaderSensor.velocity

        // Calculate leader applied voltage
        inputs.leaderAppliedVoltage = leaderSparkMax.busVoltage.volts * leaderSparkMax.appliedOutput

        inputs.leaderStatorCurrent = leaderSparkMax.outputCurrent.amps

        // Calculate leader supply current
        inputs.leaderSupplyCurrent =
            inputs.leaderStatorCurrent * leaderSparkMax.appliedOutput.absoluteValue

        inputs.leaderTempCelcius = leaderSparkMax.motorTemperature.celsius

        // Calculate follower applied voltage
        inputs.followerAppliedVoltage = leaderSparkMax.busVoltage.volts * followerSparkMax.appliedOutput

        inputs.followerStatorCurrent = followerSparkMax.outputCurrent.amps

        inputs.followerSupplyCurrent =
            inputs.followerStatorCurrent * followerSparkMax.appliedOutput.absoluteValue

        inputs.followerTempCelcius = followerSparkMax.motorTemperature.celsius

        // Log leader raw rotations for debugging
        Logger.recordOutput("Manipulator/leaderRawRotations", leaderSparkMax.encoder.position) 
    }

    /**
     * Sets the voltage of the manipulator motors.
     */
    override fun setOutputVoltage(voltage: ElectricalPotential) {
        leaderSparkMax.setVoltage(voltage.inVolts) 
    }

    /**
     * Sets the target position for the leader motor using the PID controller.
     */
    override fun setPosition(position: Length, feedforward: ElectricalPotential) {
        leaderPIDController.setReference(
            leaderSensor.positionToRawUnits(
                clamp(
                    position,
                    ManipulatorConstants.MANIPULATOR_SOFT_LIMIT_RETRACTION,
                    ManipulatorConstants.MANIPULATOR_SOFT_LIMIT_EXTENSION
                )
            ),
            CANSparkMax.ControlType.kPosition,
            0,
            feedforward.inVolts, // Feedforward is not currently used
        )
    }

    /**
     * Resets the encoder position of both motors to zero.
     */
    override fun zeroEncoder() {
        leaderSparkMax.encoder.position = 0.0
        followerSparkMax.encoder.position = 0.0
    }

    /**
     * updates the PID controller values using the sensor measurement for proportional intregral and
     * derivative gain multiplied by the 3 PID constants
     *
     * @param kP a constant which will be used to scale the proportion gain
     * @param kI a constant which will be used to scale the integral gain
     * @param kD a constant which will be used to scale the derivative gain
     */
    override fun configPID(
        kP: ProportionalGain<Meter, Volt>,
        kI: IntegralGain<Meter, Volt>,
        kD: DerivativeGain<Meter, Volt>
    ) {
        leaderPIDController.p = leaderSensor.proportionalPositionGainToRawUnits(kP)
        leaderPIDController.i = leaderSensor.integralPositionGainToRawUnits(kI)
        leaderPIDController.d = leaderSensor.derivativePositionGainToRawUnits(kD)
    }
    /**
     * Sets the output voltage of the roller motor.
     *
     * @param power The desired output power for the roller motor.
     */
    override fun setRollerPower(power: Double) {
        // Assuming you have a separate CANSparkMax object for the roller motor:
        rollerSparkMax.setOutput(power) 
    }

    /**
     * Sets the voltage of the arm motor.
     *
     * @param voltage The desired voltage for the arm motor.
     */
    override fun setArmVoltage(voltage: ElectricalPotential) {
        leaderSparkMax.setVoltage(voltage.inVolts) 
    }

    /**
     * Sets the brake mode for the roller motor.
     *
     * @param brake True to enable brake mode, false to enable coast mode.
     */
    override fun setRollerBrakeMode(brake: Boolean) {
        // Assuming you have a separate CANSparkMax object for the roller motor:
        if (brake) {
            rollerSparkMax.idleMode = CANSparkMax.IdleMode.kBrake 
        } else {
            rollerSparkMax.idleMode = CANSparkMax.IdleMode.kCoast 
        }
    }

    /**
     * Sets the brake mode for the arm motor.
     *
     * @param brake True to enable brake mode, false to enable coast mode.
     */
    override fun setArmBrakeMode(brake: Boolean) {
        if (brake) {
            leaderSparkMax.idleMode = CANSparkMax.IdleMode.kBrake 
        } else {
            leaderSparkMax.idleMode = CANSparkMax.IdleMode.kCoast 
        }
    }


}
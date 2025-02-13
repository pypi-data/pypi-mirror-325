from enum import StrEnum

from pydantic import GetJsonSchemaHandler
from pydantic.json_schema import JsonSchemaValue
from pydantic_core import CoreSchema


class Resource(StrEnum):
    PROFILE = "profile"
    ACTIVITY = "activity"
    SLEEP = "sleep"
    BODY = "body"
    WORKOUTS = "workouts"
    WORKOUT_STREAM = "workout_stream"
    CONNECTION = "connection"
    ORDER = "order"
    RESULT = "result"
    APPOINTMENT = "appointment"
    GLUCOSE = "glucose"
    HEARTRATE = "heartrate"
    HEARTRATE_VARIABILITY = "hrv"
    HRV = "hrv"
    IGE = "ige"
    IGG = "igg"
    BLOOD_OXYGEN = "blood_oxygen"
    BLOOD_PRESSURE = "blood_pressure"
    CHOLESTEROL = "cholesterol"
    DEVICE = "device"
    WEIGHT = "weight"
    FAT = "fat"
    BODY_TEMPERATURE = "body_temperature"
    BODY_TEMPERATURE_DELTA = "body_temperature_delta"
    MEALS = "meal"
    WATER = "water"
    CAFFEINE = "caffeine"
    MINDFULNESS_MINUTES = "mindfulness_minutes"
    STEPS = "steps"
    CALORIES_ACTIVE = "calories_active"
    DISTANCE = "distance"
    FLOORS_CLIMBED = "floors_climbed"
    RESPIRATORY_RATE = "respiratory_rate"
    VO2_MAX = "vo2_max"
    CALORIES_BASAL = "calories_basal"
    STRESS_LEVEL = "stress_level"
    MENSTRUAL_CYCLE = "menstrual_cycle"
    SLEEP_CYCLE = "sleep_cycle"

    ELECTROCARDIOGRAM = "electrocardiogram"
    ELECTROCARDIOGRAM_VOLTAGE = "electrocardiogram_voltage"
    AFIB_BURDEN = "afib_burden"
    HEART_RATE_ALERT = "heart_rate_alert"

    WORKOUT_DURATION = "workout_duration"
    INSULIN_INJECTION = "insulin_injection"
    CARBOHYDRATES = "carbohydrates"
    NOTE = "note"

    # Deprecated resource types:
    SLEEP_STREAM = "sleep_stream"
    HYPNOGRAM = "hypnogram"

    @classmethod
    def __get_pydantic_json_schema__(
        cls, core_schema: CoreSchema, handler: GetJsonSchemaHandler
    ) -> JsonSchemaValue:
        schema = handler(core_schema)
        # SDK Codegen backward compatibility
        schema["title"] = "ClientFacingResource"
        schema["x-fern-type-name"] = "ClientFacingResource"
        return schema

    @property
    def is_timeseries(self) -> bool:
        match self:
            case (
                Resource.PROFILE
                | Resource.ACTIVITY
                | Resource.SLEEP
                | Resource.WORKOUTS
                | Resource.WORKOUT_STREAM
                | Resource.CONNECTION
                | Resource.ORDER
                | Resource.DEVICE
                | Resource.MEALS
                | Resource.BODY
                | Resource.APPOINTMENT
                | Resource.RESULT
                | Resource.MENSTRUAL_CYCLE
                | Resource.SLEEP_STREAM
                | Resource.SLEEP_CYCLE
                | Resource.ELECTROCARDIOGRAM
            ):
                return False
            case _:
                return True

from .cohesive_columns_value import CohesiveColumnsValue
from .compare_columns_value import CompareColumnsValue
from .french_gps_coordinates import FrenchGPSCoordinates
from .french_siren_value import FrenchSirenValue
from .french_siret_value import FrenchSiretValue
from .nomenclature_actes_value import NomenclatureActesValue
from .one_of_required import OneOfRequired
from .opening_hours_value import OpeningHoursValue
from .phone_number_value import PhoneNumberValue
from .sum_columns_value import SumColumnsValue
from .year_interval_value import YearIntervalValue

# Please keep the below dict up-to-date
available_checks = {
    CohesiveColumnsValue.type: CohesiveColumnsValue,
    CompareColumnsValue.type: CompareColumnsValue,
    FrenchGPSCoordinates.type: FrenchGPSCoordinates,
    FrenchSirenValue._format_type: FrenchSirenValue,
    FrenchSiretValue._format_type: FrenchSiretValue,
    NomenclatureActesValue._format_type: NomenclatureActesValue,
    OpeningHoursValue._format_type: OpeningHoursValue,
    PhoneNumberValue._format_type: PhoneNumberValue,
    SumColumnsValue.type: SumColumnsValue,
    YearIntervalValue.type: YearIntervalValue,
    OneOfRequired.type: OneOfRequired,
}

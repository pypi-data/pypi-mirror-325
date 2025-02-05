from base_aux.aux_eq.m2_eq_validator import *
from base_aux.aux_types.m0_types import TYPE__KWARGS_FINAL


# =====================================================================================================================
@final
class EqValidChain(EqValid_Base):
    V_ARGS: tuple[EqValid_Base, ...]
    V_KWARGS: TYPE__KWARGS_FINAL    # TODO: add params for AllTrue/Any*/False*

    def validate(self, other_draft: Any) -> bool:
        other_final = other_draft

        for eq_i in self.V_ARGS:
            if eq_i != other_final:
                return False

            other_final = eq_i.OTHER_RESULT

        return True


# =====================================================================================================================
if __name__ == "__main__":
    pass


# =====================================================================================================================

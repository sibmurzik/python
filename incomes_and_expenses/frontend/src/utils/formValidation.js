export class FormValidation {
    static password = '';
    static isValid ( value, type ) {
        if ( ! value ) {
            return false;
        }
        let regEx = ""
        if ( type === 'email' ) {
            regEx = /^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$/;
        } else if ( type === 'password' ) {
            regEx = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@$!%*?&#]).{8,}$/ ;
        } else if ( type === 'name' ) {
            regEx = /^[a-zA-Zа-яёА-Яё]+$/
        } else if ( type === 'confirmPassword' ) {
            if (value !== this.password) {
                return false;
            } else {
                return true;
            }
        }
        return regEx.test( value );
    }

    static formFieldsValidation(fields) {

        if ( fields && fields.length > 0 ) {
            let validForm = true;
            for ( let i = 0; i < fields.length; i++) {

                if ( this.isValid(fields[i].inputFiled.value, fields[i].inputType) ) {
                    fields[i].inputFiled.classList.remove( "is-invalid" );
                    fields[i].inputFiled.classList.add( "is-valid" );
                    fields[i].validationFeedback.style.display = "none";
                    if (fields[i].inputType === "password" ) {
                       this.password =  fields[i].inputFiled.value
                    }
                }
                else {
                    fields[i].inputFiled.classList.remove( "is-valid" );
                    fields[i].inputFiled.classList.add( "is-invalid" );
                    fields[i].validationFeedback.style.display = "block";
                    validForm = false;
                }
            }
            return validForm;
        }
        return false;
    }


}
/**
 * A modal dialog.
 *
 * TODO: Complete
 *
 * Block component
 *
 * @element dialog
 */
class dialog extends shared {

     /**
     * shows the dialog
     * @type {bool, default property}
     */
     open;

    /**
     * name of a function that will be triggered.<br> parameters of that function are all optional:<ul><li>gui instance</li><li>id</li><li>action</li></ul><br>if cancel_action is empty, the button is not shown
     * @type {str}
     */
     cancel_action = ""

    /**
     * text of the cancel button
     * @type {str}
     */
     cancel_label = "Cancel"

    /**
     * name of a function that will be triggered.<br> parameters of that function are all optional:<ul><li>gui instance</li><li>id</li><li>action</li></ul>
     * @type {str}
     */
     validate_action = "validate"

    /**
     * text of the validate button
     * @type {str}
     */
     validate_label = "Validate"

    /**
     * a Partial object that holds the content of the dialog<br>should not be defined if page_id is set
     * @type {Partial}
     */
     partial

     /**
      * a page id to show as the content of the dialog<br>should not be defined if partial is set
      * @type {str}
      */
     page_id

}

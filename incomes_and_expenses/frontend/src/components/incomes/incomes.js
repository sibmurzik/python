import {Balances} from "../ballance_category/ballance_category";

export class Incomes extends Balances{
    constructor(sideMenuInstance, openNewRoute) {
        super(openNewRoute);

        this.incomesCategories = [
            {
                id: 1,
                title: 'Депозиты',
                element: null,
                editButton: null,
                deleteButton: null,

            },
            {
                id: 2,
                title: 'Зарплата',
                element: null,
                editButton: null,
                deleteButton: null,
            },
            {
                id: 3,
                title: 'Сбережения',
                element: null,
                editButton: null,
                deleteButton: null,
            },
            {
                id: 4,
                title: 'Инвестиции',
                element: null,
                editButton: null,
                deleteButton: null,
            },
        ]

        if (sideMenuInstance) {
            sideMenuInstance.paintActiveElement("incomesPage");
        }

        this.addCategoryButton.addEventListener('click', e => {
            openNewRoute("/incomes/create");
        })

       this.renderPage(this.incomesCategories , "incomes");
        //console.log(this.incomesCategories);


    }





    editCategory(id, title) {
        this.openNewRoute("incomes/edit?id="+ id+"&title="+title);
    }

    deleteHttpRequest(id) {
        this.deleteWindow.style.display = "none";
        document.body.style.background = "#fff";
        console.log("Deleting request to server", id)
    }






}
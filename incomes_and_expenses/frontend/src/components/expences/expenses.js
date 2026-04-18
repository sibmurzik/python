import {Balances} from "../ballance_category/ballance_category";

export class Expenses extends Balances{
    constructor(sideMenuInstance, openNewRoute) {
        super(openNewRoute);



        this.expensesCategories = [
            {
                id: 1,
                title: 'Еда',
                element: null,
                editButton: null,
                deleteButton: null,

            },
            {
                id: 2,
                title: 'Жильё',
                element: null,
                editButton: null,
                deleteButton: null,
            },
            {
                id: 3,
                title: 'Здоровье',
                element: null,
                editButton: null,
                deleteButton: null,
            },
            {
                id: 4,
                title: 'Кафе',
                element: null,
                editButton: null,
                deleteButton: null,
            },

            {
                id: 5,
                title: 'Авто',
                element: null,
                editButton: null,
                deleteButton: null,
            },
            {
                id: 6,
                title: 'Одежда',
                element: null,
                editButton: null,
                deleteButton: null,
            },
            {
                id: 7,
                title: 'Развлечения',
                element: null,
                editButton: null,
                deleteButton: null,
            },
            {
                id: 8,
                title: 'Счета',
                element: null,
                editButton: null,
                deleteButton: null,
            },
            {
                id: 9,
                title: 'Спорт',
                element: null,
                editButton: null,
                deleteButton: null,
            },


        ]

        if (sideMenuInstance) {
            sideMenuInstance.paintActiveElement("expensesPage");
        }

        this.addCategoryButton.addEventListener('click', e => {
            openNewRoute("/expenses/create");
        })

       this.renderPage(this.expensesCategories, "expenses");
        //console.log(this.incomesCategories);


    }





    editCategory(id, title) {
        this.openNewRoute("expenses/edit?id="+ id+"&title="+title);
    }

    deleteHttpRequest(id) {
        this.deleteWindow.style.display = "none";
        document.body.style.background = "#fff";
        console.log("Deleting request to server", id)
    }


}
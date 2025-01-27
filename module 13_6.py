#"Инлайн клавиатуры"

from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, Message
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup(resize_keyboard=True)
button1 = KeyboardButton(text='Рассчитать')
button2 = KeyboardButton(text='Информация')
kb.add(button1)
kb.add(button2)

inline_kb = InlineKeyboardMarkup(resize_keyboard=True)
inline_button1 = InlineKeyboardButton(text='Рассчитать норму калорий' ,callback_data='calories')
inline_button2 = InlineKeyboardButton(text='Формулы расчёта' , callback_data='formulas')
inline_kb.add(inline_button1)
inline_kb.add(inline_button2)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands=['start'])
async def start(message: Message):
    await message.answer(text="Hello", reply_markup=kb)


@dp.message_handler(text='Информация')
async def information(message: Message):
    await message.answer("This is bot for calculation of optimal calories")


@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer(text="Выберите опцию:" , reply_markup= inline_kb)

@dp.callback_query_handler(text = 'formulas')
async  def get_formulas(call: CallbackQuery):
    await call.message.answer('Формула Миффлина-Сан Жеора для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5;')
    await call.answer()


@dp.callback_query_handler(text ='calories')
async def set_age(call:CallbackQuery):
    await call.message.answer('Введите свой возраст:')
    await call.answer()
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer("Введите свой рост: ")
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message: Message, state: FSMContext):
    await state.update_data(growth=message.text)
    await message.answer("Введите свой вес: ")
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message: Message, state: FSMContext):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    try:
        age = int(data['age'])
        growth = int(data['growth'])
        weight = int(data['weight'])
    except ValueError as e:
        await message.answer(f"You have sent incorrect date {e}")
    else:
        calories = 10 * weight + 6.25 * growth - 5 * age + 5
        await message.answer(f"Your optimal daily calories is: {calories}")
    finally:
        await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

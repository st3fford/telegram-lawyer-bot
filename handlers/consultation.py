from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from states import ConsultationFSM
from database import AsyncSessionLocal
from models import Consultation
from sqlalchemy import select

router = Router()


@router.message(lambda m: m.text == "📅 Запис на консультацію")
async def start_consultation(message: Message, state: FSMContext):
    await message.answer("Введіть ваше імʼя:")
    await state.set_state(ConsultationFSM.name)


@router.message(ConsultationFSM.name)
async def get_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Введіть номер телефону:")
    await state.set_state(ConsultationFSM.phone)


@router.message(ConsultationFSM.phone)
async def get_phone(message: Message, state: FSMContext):
    await state.update_data(phone=message.text)
    await message.answer("Введіть дату (наприклад 2026-02-10):")
    await state.set_state(ConsultationFSM.date)


@router.message(ConsultationFSM.date)
async def get_date(message: Message, state: FSMContext):
    await state.update_data(date=message.text)
    await message.answer("Введіть час (наприклад 15:00):")
    await state.set_state(ConsultationFSM.time)


@router.message(ConsultationFSM.time)
async def get_time(message: Message, state: FSMContext):
    data = await state.get_data()

    async with AsyncSessionLocal() as session:
        result = await session.execute(
            select(Consultation).where(
                Consultation.date == data["date"],
                Consultation.time == message.text
            )
        )
        if result.scalar():
            await message.answer("⛔ Цей час вже зайнятий")
            return

    await state.update_data(time=message.text)
    await message.answer("Формат консультації: онлайн / офлайн")
    await state.set_state(ConsultationFSM.format)


@router.message(ConsultationFSM.format)
async def finish(message: Message, state: FSMContext):
    data = await state.get_data()

    async with AsyncSessionLocal() as session:
        session.add(
            Consultation(
                name=data["name"],
                phone=data["phone"],
                date=data["date"],
                time=data["time"],
                format=message.text
            )
        )
        await session.commit()

    await message.answer("✅ Ви успішно записані!")
    await state.clear()

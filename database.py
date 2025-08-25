from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker

### Database configuration for SQLAlchemy with async support
DATABASE_URL = "sqlite+aiosqlite:///./database.db"

# Create an async engine
engine = create_async_engine(DATABASE_URL, echo=True)

### Criar an async session
AsyncSessionLocal = async_sessionmaker(
    autocommit=False,  # Não comitar automaticamente
    autoflush=False,  # Não flush automático
    bind=engine, 
    class_=AsyncSession
)

async def get_db_session():
    ### Funcão para injetar a sessão do banco de dados
    ### É um gerador que cria uma sessão e a fecha após o uso
    ### Evita problemas de corromper arquivos, banco de dados e performance

    async with AsyncSessionLocal() as session:
        print("Antes de abrir a conexão com o banco de dados")
        yield session
        print("Depois de fechar a conexão com o banco de dados")
        await session.close()